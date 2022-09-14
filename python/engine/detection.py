# Copyright (c) 2022 Imagination Technologies Ltd.
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

import numpy as np
from .common import BaseArch
from metric.cocometrics import CocoMetrics


class Detection(BaseArch):
    def __init__(self, config):
        super().__init__(config)
        self.metrics = CocoMetrics(config['Metric']['image_size'], config["Metric"]['dataset'])

    def statistic(self, bboxes, scores, preds, targets):
        self.metrics.statistic(bboxes, scores, preds, targets)

    def summarise(self):
        summ = self.metrics()
        print(summ)

