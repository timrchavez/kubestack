#!/usr/bin/env python
"""
Copyright 2015 Reverb Technologies, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


class V1beta1_ContainerPort(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        self.swaggerTypes = {
            
            'containerPort': 'int',
            
            
            'hostIP': 'str',
            
            
            'hostPort': 'int',
            
            
            'name': 'str',
            
            
            'protocol': 'V1beta1_Protocol'
            
        }

        
        #number of port to expose on the pod&#39;s IP address
        
        self.containerPort = None # int
        
        #host IP to bind the port to
        
        self.hostIP = None # str
        
        #number of port to expose on the host; most containers do not need this
        
        self.hostPort = None # int
        
        #name for the port that can be referred to by services; must be a DNS_LABEL and unique without the pod
        
        self.name = None # str
        
        #protocol for port; must be UDP or TCP; TCP if unspecified
        
        self.protocol = None # V1beta1_Protocol
        
