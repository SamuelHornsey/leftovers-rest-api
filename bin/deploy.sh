echo 'deploying function' $1

aws lambda update-function-code --function-name $1 --zip-file fileb:///tmp/function.zip