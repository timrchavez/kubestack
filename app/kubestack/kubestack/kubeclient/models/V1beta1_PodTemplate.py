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


class V1beta1_PodTemplate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        self.swaggerTypes = {
            
            'annotations': 'V1beta1_PodTemplate_annotations',
            
            
            'desiredState': 'V1beta1_PodState',
            
            
            'labels': 'V1beta1_PodTemplate_labels',
            
            
            'nodeSelector': 'V1beta1_PodTemplate_nodeSelector'
            
        }

        
        #map of string keys and values that can be used by external tooling to store and retrieve arbitrary metadata about pods created from the template
        
        self.annotations = None # V1beta1_PodTemplate_annotations
        
        #specification of the desired state of pods created from this template
        
        self.desiredState = None # V1beta1_PodState
        
        #map of string keys and values that can be used to organize and categorize the pods created from the template; must match the selector of the replication controller to which the template belongs; may match selectors of services
        
        self.labels = None # V1beta1_PodTemplate_labels
        
        #a selector which must be true for the pod to fit on a node
        
        self.nodeSelector = None # V1beta1_PodTemplate_nodeSelector
        
