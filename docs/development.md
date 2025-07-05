# 开发指南

## 一、用户安装

```bash
pip install uv
uv pip install -U chico_dico
```

## 二、开发者安装

1）创建虚拟环境

```bash
# 创建虚拟环境
mamba create -n magic_env python=3.12

# 激活虚拟环境
conda activate magic_env

# 显示当前所有虚拟环境
conda info --envs

# 退出虚拟环境
conda deactivate

# 移除虚拟环境 magic_env
conda env remove --name magic_env
```

2）使用源代码（或 `local wheel`）安装 Python 包

```bash
# 检查 chico_dico 是否已经安装
pip list | grep chico_dico

# 从源代码安装
pip install -e .

# 从 local wheel 安装
# `pip install dist/chico_dico-[VERSION]-py3-none-any.whl`

# 卸载
pip uninstall chico_dico

# 卸载并重新安装
pip uninstall chico_dico -y && pip install -e .
```

3）功能测试

```bash
# 安装 pytest
uv pip install -U pytest

# 使用 pytest 运行测试
pytest

# 安装 nox
uv pip install -U nox

# 使用 nox 行测试
nox
```

4）格式检查

```bash
# 安装 flake8
uv pip install -U flake8
uv pip install -U flake8-import-order

# 运行格式检查
flake8 --import-order-style google
```

5）安装依赖

```bash
# 首先来到项目根目录（如已在请忽略）
cd chico_dico_magic

# 安装所有必要的依赖
pip install -r requirements.txt
```

## 三、贡献方法

1）构建 Python 包

```bash
uv pip install -U build
python -m build
```

2）上传 Python 包

```bash
uv pip install -U twine
twine upload dist/*
```
