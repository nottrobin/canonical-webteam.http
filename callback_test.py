import responses
import requests
import time

def response_callback(resp):
        time.sleep(2)
        import ipdb; ipdb.set_trace()
        resp.callback_processed = True
        return resp

with responses.RequestsMock(response_callback=response_callback) as m:
        m.add(responses.GET, 'http://example.com', body=b'test')
        resp = requests.get('http://example.com', timeout=3)
        assert resp.text == "test"
        assert hasattr(resp, 'callback_processed')
        assert resp.callback_processed is True
        import ipdb; ipdb.set_trace()
        pass
