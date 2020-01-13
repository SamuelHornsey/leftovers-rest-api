# install dependencies to a tmp dir
pip install -r requirements.txt --target /tmp/package

# copy script
cp ./main.py /tmp/package/main.py

# zip the folder
pushd /tmp/package
zip -r9 /tmp/function.zip .
popd