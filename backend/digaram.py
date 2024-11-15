from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.storage import S3
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Mongodb
from diagrams.generic.network import Firewall
from diagrams.programming.language import Nodejs

with Diagram("Cloud Share Architecture", show=True, direction="TB"):
    client = Client("User")

    with Cluster("API Gateway"):
        api_gateway = Nodejs("API Gateway")

    with Cluster("Auth Service"):
        auth_service = Nodejs("Auth Service")
        auth_db = Mongodb("User Database")

    with Cluster("File Management Service"):
        file_service = Nodejs("File Management Service")
        metadata_db = Mongodb("Metadata Database")
        s3_storage = S3("AWS S3 Storage")

    with Cluster("Sharing Service"):
        sharing_service = Nodejs("Sharing Service")
        sharing_db = Mongodb("Sharing Database")

    # Connections
    client >> api_gateway
    api_gateway >> auth_service >> auth_db
    api_gateway >> file_service
    file_service >> metadata_db
    file_service >> s3_storage
    api_gateway >> sharing_service
    sharing_service >> sharing_db
