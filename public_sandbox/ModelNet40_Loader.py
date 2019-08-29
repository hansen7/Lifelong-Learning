#  Copyright (c) 2019. Hanchen Wang
#  Last Modified: 29/08/2019, 15:03
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os, h5py
import numpy as np, pandas as pd


class ModelNetDataSet:
    def __init__(self,
                 root_dir,
                 model_dir,
                 batch=2048,
                 npoints=2048,
                 indice_gen=False,
                 convert=False,
                 data_aug_times=0):
        self.npoints = npoints
        self.root = root_dir
        self.model_dir = model_dir
        self.batch = batch
        self.data_aug_times = data_aug_times
        self.trainfns = []

        if convert:
            self._fix_offfile()
        if indice_gen:
            self._gen_indexfile()

        des_dir = os.path.join(self.model_dir, 'des')

        with open(os.path.join(des_dir, 'trainval.txt'), 'r') as f:
            for line in f:
                self.trainfns.append(line.strip())

        self.cat = {}
        with open(os.path.join(des_dir, 'modelnet_id.txt'), 'r') as f:
            for line in f:
                ls = line.strip().split()
                self.cat[ls[1]] = int(ls[0])

        self.classes = list(self.cat.keys())

    def _gen_indexfile(self):
        print('Start Generating Index Files')
        des_dir = os.path.join(self.model_dir, 'des')
        if not os.path.exists(des_dir):
            os.mkdir(des_dir)

        classes = []
        train_fs = []
        test_fs = []
        df = pd.DataFrame([], columns=['class',
                                       'train or test',
                                       'filename',
                                       'number of vertices',
                                       'number of faces'])
        feed_dict = {'class': 'none', 'train or test': 'none',
                     'filename': 'none', 'number of vertices': 0, 'number of faces': 0}
        for root, dirs, files in os.walk(self.root, topdown=False):
            print(root, dirs)
            tail = root.split('/')[-1]

            if 'train' == tail or 'test' == tail:
                for name in files:
                    if ".off" in name:
                        # print(name)
                        verts, faces = self._read_off(os.path.join(root, name))
                        feed_dict['class'] = name.split('_')[0]
                        feed_dict['train or test'] = tail
                        feed_dict['filename'] = name
                        feed_dict['number of vertices'] = len(verts)
                        feed_dict['number of faces'] = len(faces)
                        # print(feed_dict)
                        eval("%s_fs.append(os.path.join(root, name).replace(self.root, \'\') + \'\\n\')" % tail)
                        # train_fs.append(os.path.join(root, name).replace(self.root, '') + '\n')
                        # test_fs.append(os.path.join(root, name).replace(self.root, '') + '\n')
                        df = df.append(feed_dict, ignore_index=True)
                        # print(df)
            elif root != self.root:
                classes.append(tail)

        classes.sort()

        with open(os.path.join(des_dir, 'modelnet_id.txt'), 'w') as f_cls:
            for idx, cls in enumerate(classes):
                f_cls.write(str(idx) + ' ' + str(cls) + '\n')
            f_cls.close()

        with open(os.path.join(des_dir, 'trainval.txt'), 'w') as f_train:
            f_train.writelines(train_fs)
            f_train.close()

        with open(os.path.join(des_dir, 'test.txt'), 'w') as f_test:
            f_test.writelines(test_fs)
            f_test.close()

        df.to_pickle(os.path.join(des_dir, 'data_sum.pkl'))
        df.to_csv(os.path.join(des_dir, 'data_sum.txt'), header=True, index=None, sep='\t', mode='w')

        print('Index Files Generated')
        return None

    def _fix_offfile(self):
        """
        to fix the format of the raw data of ModelNet dataset downloaded from:
            http://modelnet.cs.princeton.edu
        """
        print('Start Fixing OFF Files')
        for root, dirs, files in os.walk(self.root, topdown=False):
            for name in files:
                if ".off" in name:
                    in_file = open(os.path.join(root, name), 'r', encoding='utf-8', errors='ignore')
                    all_lines = in_file.readlines()
                    tokens = all_lines[0].split()
                    # should have only one token: OFF
                    # some files has tokens as OFFx1 y1 z1
                    if len(tokens) > 1:
                        tokens[0] = tokens[0].split("OFF")[1]
                        all_lines = ["OFF\n", tokens[0] + " " + tokens[1] + " " + tokens[2] + "\n"] + all_lines[1:]
                        in_file.close()
                        out_file = open(os.path.join(root, name), 'w', encoding='utf-8', errors='ignore')
                        out_file.writelines(all_lines)
                        out_file.close()
                        print("> file: " + name + ' converted')
                    else:
                        in_file.close()

        print('OFF Files Convert Completed')
        return None

    def _read_off(self, file):
        """
        adapted from http://3dvision.princeton.edu/pvt/patch2ply.m
        """
        # print(file.readline().strip())
        f_read = open(file, 'r', encoding='utf-8', errors='ignore')
        header = f_read.readline().strip()
        if 'OFF' != header:
            print(f_read.name)
            print(header)
            raise TypeError('Not a valid OFF header')

        n_verts, n_faces, n_edges = tuple([int(s) for s in f_read.readline().strip().split(' ')])
        combined = [[float(s) for s in f_read.readline().strip().split(' ')] for idx in range(n_verts + n_faces)]

        verts = [[float(s) for s in combined[i_vert]] for i_vert in range(n_verts)]
        faces = [[int(s) for s in combined[i_face]][1:] for i_face in range(n_verts, n_verts + n_faces)]

        return np.array(verts).astype(np.float32), np.array(faces).astype(np.int32)

    def _off2ply(self, offfile, output_dir):
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        filename = offfile.split('/')[-1].replace('.off', '')
        verts, faces = self._read_off(offfile)
        v_x, v_y = verts.shape
        f_x, f_y = faces.shape
        # verts -> n_points * 3 array for coordinates
        # faces -> n_faces * 3 for triangle meshes

        with open(os.path.join(output_dir, filename + '.ply'), 'w') as out_ply:
            out_ply.write('ply\n')
            out_ply.write('format ascii 1.0 \n')
            out_ply.write('comment made by Hanchen Wang, hc.wang96@gmail.com\n')

            out_ply.write('element vertex %d\n' % v_x)
            out_ply.write('property float x\n')
            out_ply.write('property float y\n')
            out_ply.write('property float z\n')

            out_ply.write('element face %d\n' % f_x)
            out_ply.write('property list uchar int vertex_index\n')
            out_ply.write('end_header\n')
            out_ply.writelines(["%s\n" % " ".join(str(item).replace('[', '').replace(']', '').split())
                                for item in verts])
            out_ply.writelines(["3 %s\n" % " ".join(str(item).replace('[', '').replace(']', '').split())
                                for item in faces])

            # out_ply.writelines(["%s\n" % " ".join(str(item).replace('[', '').replace(']', '').split())
            #                     for item in coords])
        return None

    def _batch_off2ply(self):

        for root, dirs, files in os.walk(self.root, topdown=False):
            for name in files:
                if ".off" in name:
                    self._off2ply(offfile=os.path.join(root, name), output_dir=root)
                    print(os.path.join(root, name), ' converted')

        print('.off files has been converted')
        return None

    def _hdf2ply(self, idx, name, hdf5file, plyfile_outdir):
        f_in = h5py.File(os.path.join(hdf5file), 'r')
        coords = np.array(f_in['data'])[idx]

        with open(os.path.join(plyfile_outdir,  name + '.ply'), 'w') as out_ply:
            out_ply.write('ply\n')
            out_ply.write('format ascii 1.0 \n')
            out_ply.write('comment made by Hanchen Wang, hc.wang96@gmail.com\n')

            out_ply.write('element vertex %d\n' % len(coords))
            out_ply.write('property float x\n')
            out_ply.write('property float y\n')
            out_ply.write('property float z\n')

            # out_ply.write('element face %d\n' % f_x)
            # out_ply.write('property list uchar int vertex_index\n')
            out_ply.write('end_header\n')

            out_ply.writelines(["%s\n" % " ".join(str(item).replace('[', '').replace(']', '').split())
                                for item in coords])
            # out_ply.writelines(["3 %s\n" % str(item).replace('[', '').replace(']', '') for item in faces])
        return None

    def _batch_hdf5_aug_guassian_noise(self, hdf5_root_dir, magnitude=0.01, augtimes=2):
        """
        augment the training data by augmenting the original data with Gaussian noise
        """
        for file in os.listdir(hdf5_root_dir):
            if '.h5' in file and 'aug_' not in file:
                '''
                the original file should a dict of ['data', 'faceId', 'label', 'normal']
                '''
                f_in = h5py.File(os.path.join(hdf5_root_dir, file), 'r')
                coords = np.array(f_in['data'])

                for idx in range(augtimes):
                    out_f_name = os.path.join(hdf5_root_dir, file.replace('.h5', '') + '_aug%d' % idx + '.h5')
                    # shutil.copy2(os.path.join(hdf5_root_dir, file), out_f_name)

                    f_out = h5py.File(out_f_name, 'w')
                    for key in f_in.keys():
                        f_out[key] = np.array(f_in.get(key))
                    del f_out['data']
                    f_out['data'] = coords + magnitude * np.random.randn(*coords.shape)
                    f_out.close()
                f_in.close()

        # update the train and test file list
        train_f = open(os.path.join(hdf5_root_dir, 'train_files.txt'), 'w')
        test_f = open(os.path.join(hdf5_root_dir, 'test_files.txt'), 'w')
        for file in os.listdir(hdf5_root_dir):
            if '.h5' in file:
                if 'train' in file:
                    train_f.write(file + '\n')
                elif 'test' in file:
                    test_f.write(file + '\n')

        train_f.close()
        test_f.close()
        return None

    def _batch_hdf5_aug_rotation(self, hdf5_root_dir, roll=None, pitch=None, yaw=None,
                                 add_gau_noise=False, mag=0.01):

        if not roll:
            roll = np.random.uniform(0, np.pi * 2)
        if not pitch:
            pitch = np.random.uniform(0, np.pi * 2)
        if not yaw:
            yaw = np.random.uniform(0, np.pi * 2)

        rot_mat_x = np.array([[1, 0, 0],
                              [0, np.cos(roll), -np.sin(roll)],
                              [0, np.sin(roll),  np.cos(roll)]])
        rot_mat_y = np.array([[ np.cos(pitch), 0, np.sin(pitch)],
                              [0, 1, 0],
                              [-np.sin(pitch), 0, np.cos(pitch)]])
        rot_mat_z = np.array([[np.cos(yaw), -np.sin(yaw), 0],
                              [np.sin(yaw),  np.cos(yaw), 0],
                              [0, 0, 1]])

        for file in os.listdir(hdf5_root_dir):
            if '.h5' in file and 'aug_' not in file:
                '''
                the original file should a dict of ['data', 'faceId', 'label', 'normal']
                '''
                f_in = h5py.File(os.path.join(hdf5_root_dir, file), 'r')
                coords = np.array(f_in['data'])

                out_f_name = os.path.join(hdf5_root_dir, file.replace('.h5', '') + '_rot_aug%d' + '.h5')

                f_out = h5py.File(out_f_name, 'w')
                for key in f_in.keys():
                    f_out[key] = np.array(f_in.get(key))
                del f_out['data']

                # rotate rotation in the Euler angle respective
                coords = coords.dot(rot_mat_x.dot(rot_mat_y@rot_mat_z))
                if add_gau_noise:
                    coords += mag * np.random.randn(*coords.shape)

                f_out['data'] = coords
                f_out.close()
                f_in.close()

        # update the train and test file list
        train_f = open(os.path.join(hdf5_root_dir, 'train_files.txt'), 'w')
        test_f = open(os.path.join(hdf5_root_dir, 'test_files.txt'), 'w')
        for file in os.listdir(hdf5_root_dir):
            if '.h5' in file:
                if 'train' in file:
                    train_f.write(file + '\n')
                elif 'test' in file:
                    test_f.write(file + '\n')

        train_f.close()
        test_f.close()

        return None

    # TODO: figure out the sampling method
    def _batch_ply2hdf5(self, plyfile_dir, batchsize):

        return None


if __name__ == '__main__':
    data_dir = r'../pointnet-master/data/ModelNet40/'
    # data_dir = r'/Users/hansen/Downloads/ModelNet40/'
    model_dir = r'../pointnet-master/'
    hdf5_root_dir = r'../pointnet-master/data/modelnet40_ply_hdf5_2048'
    my_dataset = ModelNetDataSet(root_dir=data_dir,
                                 model_dir=model_dir,
                                 indice_gen=True,
                                 convert=True)
    # my_dataset._batch_hdf5_aug_guassian_noise(hdf5_root_dir=hdf5_root_dir)
    my_dataset._batch_off2ply()


