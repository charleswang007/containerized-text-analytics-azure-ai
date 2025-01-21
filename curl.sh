curl --location APPLICATION_URL/analyze  \
--header 'Content-Type: application/json' \
--data '{
"documents": [
    {
    "text": "Hello world, this is a simple input",
    "id": "1",
    "language": "en",
    "isLanguageDefaulted": false,
    "isLanguageFinalized": true,
    "isAutoLanguageDetectionEnabled": false
    },
    {
    "text": "It'\''s incredibly sunny outside! I'\''m so happy.",
    "id": "2-en",
    "language": "en",
    "isLanguageDefaulted": false,
    "isLanguageFinalized": true,
    "isAutoLanguageDetectionEnabled": false
    },
    {
    "text": "Pike place market is my favorite Seattle attraction.",
    "id": "3-en",
    "language": "en",
    "isLanguageDefaulted": false,
    "isLanguageFinalized": true,
    "isAutoLanguageDetectionEnabled": false
    }
]
}'
