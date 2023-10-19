import logging


def setup_logging(log_file_path):
    # 创建一个logger实例
    logger = logging.getLogger("RTL Utils")
    logger.setLevel(logging.DEBUG)

    # 创建文件处理器，用于将日志写入文件
    file_handler = logging.FileHandler(log_file_path, mode="w")
    file_handler.setLevel(logging.DEBUG)

    # 创建控制台处理器，用于将日志输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 创建日志格式器
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # 将格式器设置给处理器
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 将处理器添加到logger实例
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
