import boto3, json
#import constants as const
region_name = 'us-east-1'
# endpoint_name = const.smjs_endpoint
endpoint_name = "<Endpoint-name>"

#MAX_LENGTH = 2048
MAX_LENGTH = 4096
NUM_RETURN_SEQUENCES = 1
TOP_K = 0
TOP_P = 0.7
DO_SAMPLE = True
CONTENT_TYPE = 'application/json'

def generate_response(prompt, temperature, top_p, max_new_tokens):
    session = boto3.Session(region_name=region_name)
    smclient = session.client('sagemaker-runtime')


    content_type = 'application/json'
    input_data = {
        "inputs": prompt,
        "parameters": {
            "do_sample": True,
            "top_p": top_p, 
            "temperature": temperature,
            "max_new_tokens": max_new_tokens,
            "stop": ["<|endoftext|>", "</s>"]
        }
    }
    payload = json.dumps(input_data)                                            # Payload for inference.
    print(f"calling SagemMaker endpoint with: {input_data}")

    response = smclient.invoke_endpoint(
        EndpointName=endpoint_name, 
#        CustomAttributes=custom_attributes, 
        ContentType=content_type,
        Body=payload
    )

    result = json.loads(response['Body'].read().decode())
    return result