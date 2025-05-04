from langchain_huggingface.embeddings import HuggingFaceEmbeddings

from src import ChopDoc

TEXT_DOC = """
One of the most important things I didn't understand about the world when I was a child is the degree to which the returns for performance are superlinear.

Teachers and coaches implicitly told us the returns were linear. "You get out," I heard a thousand times, "what you put in." They meant well, but this is rarely true. If your product is only half as good as your competitor's, you don't get half as many customers. You get no customers, and you go out of business.

It's obviously true that the returns for performance are superlinear in business. Some think this is a flaw of capitalism, and that if we changed the rules it would stop being true. But superlinear returns for performance are a feature of the world, not an artifact of rules we've invented. We see the same pattern in fame, power, military victories, knowledge, and even benefit to humanity. In all of these, the rich get richer. [1]
"""

TEXT_PYTHON = """
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

for i in range(10):
    print (i)
"""

TEXT_MARKDOWN = """
# Fun in California

## Driving

Try driving on the 1 down to San Diego

### Food

Make sure to eat a burrito while you're there

## Hiking

Go to Yosemite
"""

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

def test_character_chunking():
    chunking = ChopDoc()
    result = chunking.character_splitter(TEXT_DOC)
    return result


def test_recursive_character_chunking():
    chunking = ChopDoc()
    result = chunking.recursive_character_splitter(TEXT_DOC)
    return result

def test_document_specific_chunking(text, type):
    chunking = ChopDoc()
    result = chunking.document_specific_splitter(text, type)
    return result

def test_semantic_chunking():
    chunking = ChopDoc()
    result = chunking.semantic_splitter(TEXT_DOC, embeddings)
    return result

print('---- Character Chunking Tests ----')
print(len(test_character_chunking()))
print('---- Recursive Character Chunking Tests ----')
print(len(test_recursive_character_chunking()))
print('---- Document Specific Chunking Tests - PYTHON ----')
print(len(test_document_specific_chunking(TEXT_PYTHON, 'python')))
print('---- Document Specific Chunking Tests - MARKDOWN ----')
print(len(test_document_specific_chunking(TEXT_MARKDOWN, 'markdown')))
print('---- Semantic Chuking Tests ----')
print(len(test_semantic_chunking()))