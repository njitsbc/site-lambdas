# site-lambdas

## Local Setup

```
aws configure

# also may need to do
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...

export AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY
```

## Pulling Lambdas from AWS Console

```
chmod +x pullLambdas.sh
./pullLambdas.sh
```

## Test Accesses By Listing All Services

```
python listAllServices.py
```