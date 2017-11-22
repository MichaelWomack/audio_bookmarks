from app.model.base.json_serializable import JsonSerializable

class AudioBook(JsonSerializable):

    def __init__(self, **kwargs):
        self._name = kwargs.get('name', None)
        self._author = kwargs.get('author', None)
        self._publish_year = kwargs.get('publishYear', None)
    
    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @property
    def publish_year(self):
        return self._publish_year

    def __repr__(self):
        return 'AudioBook(name={name}, author={author} publishYear={publish_year})'.format(name=self.name,
                author=self.author,
                publish_year=self.publish_year
        )


    def json(self):
        return {
            'name': self.name,
            'author': self.author,
            'publishYear': self.publish_year,
        }
