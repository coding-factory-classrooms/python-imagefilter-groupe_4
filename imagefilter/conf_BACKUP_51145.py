import argparse
import configparser
import logger

config = configparser.ConfigParser()
config.read('imagefilter.ini')

<<<<<<< HEAD:imagefilter/imagesvg/conf.py


=======
>>>>>>> d9ff5451c52c510191eb216ee4099aef7981eba5:imagefilter/conf.py

def load_conf():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--conf-file', type=str,
                        help='Configuration ini file')
    parser.add_argument('-i', '--input-dir', type=str,
                        help='Path to input directory of images')
    parser.add_argument('-o', '--output-dir', type=str,
                        help='Path to output directory of images')
    parser.add_argument('-f', '--filters', type=str,
                        help='List of filters to apply')
    parser.add_argument('-l', '--log-file', type=str,
                        default=logger.log_file,
                        help='log file')
    parser.add_argument('-lf', '--list_filters', action='store_true',
                        help='Display supported filters')

    args = parser.parse_args()

    if args.list_filters:
        print_filters()
        exit(0)

    if args.conf_file:
        conf = conf_from_inifile(args.conf_file)
    else:
        conf = {}

    if args.input_dir:
        conf['input_dir'] = args.input_dir

    if args.output_dir:
        conf['output_dir'] = args.output_dir

    if args.filters:
        conf['filters'] = args.filters

    if args.log_file:
        conf['log_file'] = args.log_file

    conf['files'] = files_from_inputdir(conf['input_dir'])

    return conf


write_config = configparser.ConfigParser()

conf_file = open("imagefilter.ini", 'w')
write_config.write(conf_file)
conf_file.close()

read_config = configparser.ConfigParser()
read_config.read("imagefilter.ini")

<<<<<<< HEAD:imagefilter/imagesvg/conf.py
=======
logger.dump_log()


>>>>>>> d9ff5451c52c510191eb216ee4099aef7981eba5:imagefilter/conf.py
