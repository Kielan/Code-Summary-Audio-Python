import os
import sys
sys.path.append(".")

def main():
    config, args = get_config()
    # exit()
    # init logger, create log dir and set log level, etc.
    if args.resume and args.test:
        raise Exception("cannot use flag --resume and --test together")
    if args.resume or args.test:
        config.logging.path = EXP_PATH = args.resume or args.test
    else:
        EXP_PATH = config_experiment_dir(config)
        init_logger(os.path.join(EXP_PATH, "log.txt"), config.logging.file_level, config.logging.console_level)
        # save config to the logger directory
        save_config_to_yaml(config)
    

    # load dataset. The valid_dataset can be None
    train_dataset, valid_dataset, test_dataset, Processor = load_dataset(config, test = args.test is not None or config.learning_setting == 'zero_shot')

    # main
    if config.learning_setting == 'full':
        res = trainer(
            EXP_PATH,
            config,
            Processor,
            resume = args.resume,
            test = args.test,
            train_dataset = train_dataset,
            valid_dataset = valid_dataset,
            test_dataset = test_dataset,
        )
        
def trainer(EXP_PATH, config, Processor, train_dataset = None, valid_dataset = None, test_dataset = None, resume = None, test = None, zero = False):
    if not os.path.exists(EXP_PATH):
        os.mkdir(EXP_PATH)
    config.logging.path = EXP_PATH
    # set seed
    set_seed(config.reproduce.seed)
    
    # load the pretrained models, its model, tokenizer, and config.
    plm_model, plm_tokenizer, plm_config, plm_wrapper_class = load_plm_from_config(config)
    
    
