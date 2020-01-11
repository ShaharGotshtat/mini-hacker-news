import requests


class Test:
    URL_BASE = 'http://0.0.0.0:5000/mini-hacker-news/api/v1'
    HEADERS = {'Content-type': 'application/json'}

    POST_ATTRIBUTES_INDICES = {
            'id': 0,
            'created_at': 1,
            'text': 2,
            'upvotes': 3,
            'downvotes': 4
        }

    post_id = -1

    def get_attribute_from_post(self, post, attribute):
        return post[0][self.POST_ATTRIBUTES_INDICES[attribute]]

    def get_post(self):
        get_post_request = requests.get(url=f'{self.URL_BASE}/post/{self.post_id}',
                                        headers=self.HEADERS)

        assert(get_post_request.status_code == 200)
        return eval(get_post_request.content)

    def test_add_post(self):
        creating_post_request = requests.post(url=f'{self.URL_BASE}/post',
                                              headers=self.HEADERS,
                                              json={"text": "This is a new post!"})

        assert(creating_post_request.status_code == 200)
        self.post_id = eval(creating_post_request.content)
        print(f'Successfully added post with id = {self.post_id}')

    def test_update_post(self):
        new_text = "This is an updated post!"
        updating_post_request = requests.put(url=f'{self.URL_BASE}/post',
                                             headers=self.HEADERS,
                                             json={"id": str(self.post_id), "text": new_text})

        assert(updating_post_request.status_code == 200)
        updated_post = self.get_post()
        post_text = self.get_attribute_from_post(updated_post, 'text')
        assert(post_text == new_text)
        print(f'Successfully updated post with id = {self.post_id}, the new text is {new_text}')

    def test_upvote_post(self):
        post_before_upvote = self.get_post()
        current_upvotes = self.get_attribute_from_post(post_before_upvote, 'upvotes')

        upvote_post_request = requests.put(url=f'{self.URL_BASE}/post/upvote',
                                           headers=self.HEADERS,
                                           json={"id": str(self.post_id)})

        assert(upvote_post_request.status_code == 200)
        upvoted_post = self.get_post()
        new_upvotes = self.get_attribute_from_post(upvoted_post, 'upvotes')
        assert(new_upvotes == current_upvotes + 1)
        print(f'Successfully upvoted post with id = {self.post_id}')

    def test_downvote_post(self):
        post_before_downvote = self.get_post()
        current_downvotes = self.get_attribute_from_post(post_before_downvote, 'downvotes')

        downvote_post_request = requests.put(url=f'{self.URL_BASE}/post/downvote',
                                             headers=self.HEADERS,
                                             json={"id": str(self.post_id)})

        assert(downvote_post_request.status_code == 200)
        downvoted_post = self.get_post()
        new_downvotes = self.get_attribute_from_post(downvoted_post, 'downvotes')
        assert(new_downvotes == current_downvotes + 1)
        print(f'Successfully downvoted post with id = {self.post_id}')

    def test_delete_post(self):
        delete_post_request = requests.delete(url=f'{self.URL_BASE}/post/{self.post_id}',
                                              headers=self.HEADERS)

        assert(delete_post_request.status_code == 200)
        assert(int(eval(delete_post_request.content)) == self.post_id)
        print(f'Successfully deleted post with id = {self.post_id}')

    def test(self):
        self.test_add_post()
        self.test_update_post()
        self.test_upvote_post()
        self.test_downvote_post()
        self.test_delete_post()


test_class = Test()
test_class.test()
