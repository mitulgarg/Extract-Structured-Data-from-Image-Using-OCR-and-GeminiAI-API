from google.cloud import language_v1

def analyze_text(text):
    client = language_v1.LanguageServiceClient()
    document = {"content": text, "type_": language_v1.Document.Type.PLAIN_TEXT}
    response = client.analyze_entities(request={'document': document})
    
    entities = []
    for entity in response.entities:
        entities.append({'name': entity.name, 'type': language_v1.Entity.Type(entity.type_).name})
    
    return entities

# Example usage:
text = "John Doe, 20th January 1990, 123 Main St, Anytown"
entities = analyze_text(text)
print(entities)
