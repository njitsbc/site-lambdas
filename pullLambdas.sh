functions=$(aws lambda list-functions --query 'Functions[*].FunctionName' --output text)

for function in $functions
do
    code_location=$(aws lambda get-function --function-name $function --query 'Code.Location' --output text)
    echo $code_location
    
    # download zip from URL stored in $code_location
    curl -o $function.zip $code_location > /dev/null
    unzip -o $function.zip > /dev/null
    rm $function.zip
    
    # move file to its own dir
    mv lambda_function.py $function.py
    mv $function.py $function/
done