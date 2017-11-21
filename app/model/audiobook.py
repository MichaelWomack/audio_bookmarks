
class AudioBook(object): 

    def __init__(self, **kwargs):
        self._name = kwargs['name']
        self._author = kwargs['author']
        self._publish_year = kwargs['publishYear']
    
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
        return 'AudioBook(\nname={name},\nauthor={author}\npublishYear={publishYear}\n)'.format(name=self.name,
                author=self.author,
                publishYear=self.publish_year
        )


if __name__ == '__main__':
    ab = AudioBook(name="The Intelligent Investor", author="Benjamin Graham", publishYear=1932)
    print ab