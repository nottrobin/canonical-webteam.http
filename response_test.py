# Core
import time

# Third party
import requests
import requests_cache
import responses


cached_request = requests_cache.CachedSession(expire_after=2)

response_1 = b"hi"
response_2 = b"hello"
response_3 = b"howdy"

# with responses.RequestsMock() as request_mock_1:
#     request_mock_1.add(responses.GET, 'http://example.com', body=response_1)
#     direct_response_1 = requests.get('http://example.com')
#     uncached_response = cached_request.get('http://example.com')
#
# with responses.RequestsMock() as request_mock_2:
#     request_mock_2.add(responses.GET, 'http://example.com', body=response_2)
#     direct_response_2 = requests.get('http://example.com')
#     cached_response = cached_request.get('http://example.com')
#
# time.sleep(2)
#
# with responses.RequestsMock() as request_mock_3:
#     request_mock_3.add(responses.GET, 'http://example.com', body=response_3)
#     direct_response_3 = requests.get('http://example.com')
#     expired_response = cached_request.get('http://example.com')


def slow_response(response):
    import ipdb; ipdb.set_trace()
    time.sleep(3)

    return response


with responses.RequestsMock(response_callback=slow_response) as request_mock_4:
    request_mock_4.add(responses.GET, 'http://example.com', body=response_3)

    import ipdb; ipdb.set_trace()

    timeout_direct_response = requests.get('http://example.com', timeout=2)
    timeout_cached_response = cached_request.get(
        'http://example.com', timeout=2
    )

# assert direct_response_1.content == response_1
# assert direct_response_2.content == response_2
# assert direct_response_3.content == response_3
#
# assert uncached_response.content == response_1
# assert cached_response.content == response_1
# assert expired_response.content == response_3

import ipdb; ipdb.set_trace()
