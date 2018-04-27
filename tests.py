import time
import unittest
import requests
import responses


class InvalidApiResponse(Exception):
    pass


@responses.activate
def test_get():
    """
    Test the get stuff
    """

    def timeout_callback(request):
        time.sleep(3)

        return (200, {}, "OK")

    responses.add_callback(
        responses.GET, 'http://example.com',
        callback=timeout_callback
    )

    requests.get('http://example.com', timeout=2)


if __name__ == '__main__':
    unittest.main()
