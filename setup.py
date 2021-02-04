import setuptools

setuptools.setup(
    name="streamlit-labelstudio",
    version="0.0.3",
    author="",
    author_email="",
    description="A Streamlit component that provides an annotation interface using the LabelStudio Frontend",
    long_description="A Streamlit component that provides an annotation interface using the LabelStudio Frontend",
    long_description_content_type="text/plain",
    url="https://github.com/deneland/streamlit-labelstudio",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
