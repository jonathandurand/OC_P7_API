import unittest
import boto3

global app_name
global region
app_name = 'my-deployment-attemp'
region = 'us-east-1'

class TestStatus(unittest.TestCase):
    def test_status(self):
        sage_client = boto3.client('sagemaker', region_name=region)
        endpoint_description = sage_client.describe_endpoint(EndpointName=app_name)
        endpoint_status = endpoint_description['EndpointStatus']
        print('Application status is {}'.format(endpoint_status))
        self.assertEqual(endpoint_status, "InService", "Should be in service")

if __name__ == '__main__':
    unittest.main()