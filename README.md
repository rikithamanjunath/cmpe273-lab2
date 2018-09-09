# cmpe273-lab2

Steps

1. Run the server from the cmpe273-lab2 directory
     #####python3 calculator/calculator_server.py
     
2. Run the client from the cmpe273-lab2 directory
     #####python3 calculator/calculator_client.py 
     
To run proto file from the cmpe273-lab2 directory

   #####python3 -m grpc_tools.protoc -Iprotos --python_out=calculator/ --grpc_python_out=calculator/ calculator.proto
