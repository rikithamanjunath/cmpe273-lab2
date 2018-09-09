# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

from calculator import calculator_pb2, calculator_pb2_grpc

def run(i,j):
  channel = grpc.insecure_channel('localhost:50051')
  stub = calculator_pb2_grpc.CalculatorStub(channel)
  response = stub.Add(calculator_pb2.RequestAdd(inputA=i,inputB=j))
  print(response.result)

if __name__ == '__main__':
    for i in range(-2,3):
        for j in range(-2,3):
            run(i,j)
