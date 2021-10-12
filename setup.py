import setuptools

def readme():   
    with open('README.md', 'r') as f:
        README = f.read()
    return README


setuptools.setup(
    name="FaceMasque",
    version="1.0.9",
    description="A Python package to classify weather a person is weared a mask or not.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Kushal0189/FaceMasque",
    author="KUSHAL MASTER",
    author_email="kushalmaster8@gmail.com",
    #data_files   = [ ("FaceMasque",  ["./FaceMasque/Copy_of_ultra_light_640.onnx",
                               # "./FaceMasque/vgg_mask.h5"])],
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        "FaceMasque.data": [
            "Copy_of_ultra_light_640.onnx",
            "vgg_mask.h5",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "onnx==1.6.0",
        "onnx-tf==1.3.0",
        "onnxruntime==0.5.0",
        "opencv-python==4.2.0.32",
        "tensorflow==1.15.2",
        "keras",
    ],
    python_requires='>=3.6',
)
