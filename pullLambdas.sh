functions=$(aws lambda list-functions --query 'Functions[*].FunctionName' --output text)

for function in $functions
# get the lambda code from within each Code.Location zip file
do
    code_location=$(aws lambda get-function --function-name $function --query 'Code.Location' --output text)
    echo $code_location
    curl -o $function.zip $code_location > /dev/null
    unzip -o $function.zip > /dev/null
    rm $function.zip
    mv lambda_function.py $function.py
    mv $function.py $function/
done