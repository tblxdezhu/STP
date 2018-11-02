process_num = 2
slam_config = "/home/roaddb/source/core/algorithm_vehicle_offlineslam/config/slamConfig.yaml"
camera_config = "/home/roaddb/source/core/vehicle/config/camera_big_lens_undistort.json"
# output_path = "/Users/test1/PycharmProjects/github/STP/test/results"
output_path = "/home/roaddb/stp_test_result"
code_path = "/media/psf/Untitled/Auto_test_SLAM/envs/env0"

cases_path = {
    'fuji': '/media/psf/Untitled/SLAM_TEST/auto_test_large/large_fuji/rtv',
    'milford': '/media/psf/Untitled/SLAM_TEST/auto_test_large/large_milford/rtv',
    'memmingen': '/media/psf/Untitled/SLAM_TEST/auto_test_large/large_memingen/rtv',
    'localtest': '/Users/test1/PycharmProjects/github/STP/test/cases',
    '16test': '/media/psf/Untitled/Auto_test_SLAM/data/16test',
    '15test': '/home/roaddb/test_data',
}

vehicle_exec = "/home/roaddb/source/core/algorithm_vehicle_offlineslam/dist/x64/bin/ZSLAMExe"
