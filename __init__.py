import os
import sys

# 获取当前文件所在目录
EXTENSION_FOLDER = os.path.dirname(os.path.realpath(__file__))
WEB_DIRECTORY = os.path.join(EXTENSION_FOLDER, "js")

class GradientTheme:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {}}
    
    RETURN_TYPES = ()
    FUNCTION = "run"
    CATEGORY = "UI"

    def __init__(self):
        # 在类初始化时输出广告信息
        ad_message = "此插件由抖音：大师兄（AIGC）打造"
        for i in range(4):
            sys.stdout.write(f"{ad_message}\n")
            sys.stdout.flush()  # 强制立即输出

    def run(self):
        return {}

# 在模块加载时也输出广告
print("\n" + "="*50)
print("此插件由抖音：大师兄（AIGC）打造")
print("此插件由抖音：大师兄（AIGC）打造")
print("此插件由抖音：大师兄（AIGC）打造")
print("此插件由抖音：大师兄（AIGC）打造")
print("="*50 + "\n")

NODE_CLASS_MAPPINGS = {
    "GradientTheme": GradientTheme
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GradientTheme": "Gradient Theme"
}

WEB_DIRS = [WEB_DIRECTORY]