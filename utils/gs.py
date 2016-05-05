#   Copyright 2015 Check Point Software Technologies LTD
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


# URI Strings
URI = "https://te.checkpoint.com/tecloud/api/v1/file/"
QUERY = "query"
UPLOAD = "upload"
DOWNLOAD = "download"
QUERY_SELECTOR = URI + QUERY
UPLOAD_SELECTOR = URI + UPLOAD
DOWNLOAD_SELECTOR = URI + DOWNLOAD

# Request Strings
MD5 = "md5"
SHA1 = "sha1"
SHA256 = "sha256"

TE = "te"
AV = "av"

PDF = "pdf"
XML = "xml"

# Response Strings
STATUS = "status"
LABEL = "label"
RESPONSE = "response"

FOUND = "FOUND"
PARTIALLY_FOUND = "PARTIALLY_FOUND"
NOT_FOUND = "NOT_FOUND"
UPLOAD_SUCCESS = "UPLOAD_SUCCESS"
PENDING = "PENDING"
NO_QUOTA = "NO_QUOTA"
FORBIDDEN = "FORBIDDEN"

BENIGN = "benign"
MALICIOUS = "malicious"
ERROR = "error"
MESSAGE = "message"


# TE Strings
TE_VERDICT = "combined_verdict"
TE_SEVERITY = "severity"
TE_CONFIDENCE = "confidence"

# AV Strings
AV_INFO = "malware_info"
AV_NAME = "signature_name"
AV_FAMILY = "malware_family"  # 0 - 5 (0-none, 1-low, 5 high)
AV_TYPE = "malware_type"
AV_SEVERITY = "severity"
AV_CONFIDENCE = "confidence"


