# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.
class Story:
    def __init__(self,story,length,morallesson,agegroup):
        self.story=story
        self.length=length
        self.morallesson=morallesson
        self.agegroup=agegroup

    def record_stories(self):
        return f"The {self.story} story of length {self.length} has {self.morallesson} moral lesson to girls aged {self.agegroup}"

class Story2(Story):
    def record_stories(self):
        return f"The {self.story} story of length {self.length} has {self.morallesson} moral lesson to girls aged {self.agegroup}"


class StoryTeller:
    def __init__(self,storyteller,story,length,morallesson,agegroup):
        self.storyteller=storyteller
        self.story=story
        self.length=length
        self.morallesson=morallesson
        self.agegroup=agegroup

    def record_stories(self):
        return f"The {self.story} is being narrated by {self.storyteller} storyteller and is of length {self.length} has {self.morallesson} to {self.agegroup}  agegroup"


class StoryTeller2(StoryTeller):
    def record_stories(self):
        return f"The {self.story} is being narrated by {self.storyteller} storyteller and is of length {self.length} has {self.morallesson} to {self.agegroup}  agegroup"


class Translator:
    





