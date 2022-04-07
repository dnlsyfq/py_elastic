from elasticsearch import Elasticsearch

es = Elasticsearch(
    ["https://satu-production.es.ap-southeast-1.aws.found.io:9243"],
    basic_auth=("satusystem", "sat@sia2021"),
)

res = es.indices.get_alias(index="*")

# print(list(dict(res).keys()))

index_name = "sda_alerts"
try:
    response = es.search(index=index_name)
    print(dict(response).keys())
    # print(response["_shards"]["total"])
    # print(response["_shards"])
    print(response)
except Exception as e:
    print(str(e))
