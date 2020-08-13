import setuptools

with open("README.md", "r") as file:
    readme = file.read()

setuptools.setup(
	name="IndianNameGenerator",
	version="4.0.0",
	author="OnkarGavali",
	author_email="onkargavali1561@gmail.com",
	description="A quick way to get indian names",
	long_description=readme,
	long_description_content_type="text/markdown",
	url="https://github.com/OnkarGavali/indian-name-generator",
	license="MIT",
	classifiers=["License :: OSI Approved :: MIT License"],
	packages=["IndianNameGenerator"],
	include_package_data=True,
	python_requires='>=3.0',

)