import os

import mlflow.pyfunc
import pandas as pd
from mlflow.models import infer_signature


class AddN(mlflow.pyfunc.PythonModel):
    def __init__(self, n):
        self.n = n

    def predict(self, context, model_input):
        return model_input.apply(lambda column: column + self.n)

    def reckon_features(self):
        pass


os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
os.environ['AWS_REGION'] = 'us-east-1'
os.environ['AWS_ACCESS_KEY_ID'] = 'test'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'test'
os.environ['MLFLOW_S3_ENDPOINT_URL'] = 'http://localhost:4000'

if __name__ == '__main__':
    mlflow.set_tracking_uri('http://test@email.com:SecurePassword@localhost')
    mlflow.create_experiment('first_experiment')
    mlflow.set_experiment('add_n_func')

    add5_model = AddN(n=5)
    training_data = pd.DataFrame([range(10)])
    # signature = infer_signature()

    with mlflow.start_run(tags={'project': 'test'}, description='my first pyfunc'):
        mlflow.pyfunc.log_model(python_model=add5_model, artifact_path='model')
