import pytest

from ....tests.utils import get_graphql_content


@pytest.mark.django_db
@pytest.mark.count_queries(autouse=False)
def test_retrieve_shop(api_client, channel_USD, count_queries):
    query = (
        """
            fragment AvailableShippingMethods on ShippingMethodType {
                id
                price {
                    amount
                }
                minimumOrderPrice {
                    amount
                    currency
                }
                name
            }
        """
        + """
        query getShop($channel: String!) {
          shop {
            defaultCountry {
              code
              country
            }
            availableShippingMethods(channel: $channel) {
              ...AvailableShippingMethods
            }
            countries {
              country
              code
            }
          }
        }
    """
    )

    get_graphql_content(
        api_client.post_graphql(query, variables={"channel": channel_USD.slug})
    )
