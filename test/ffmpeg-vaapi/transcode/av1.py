###
### Copyright (C) 2022 Intel Corporation
###
### SPDX-License-Identifier: BSD-3-Clause
###

from ....lib import *
from ....lib.ffmpeg.vaapi.util import *
from ....lib.ffmpeg.vaapi.transcoder import TranscoderTest

spec = load_test_spec("av1", "transcode")

class default(TranscoderTest):
  @slash.parametrize(("case"), sorted_by_resolution(spec))
  def test(self, case):
    vars(self).update(spec[case].copy())
    vars(self).update(
      case  = case,
      codec = "av1",
    )
    self.transcode()

