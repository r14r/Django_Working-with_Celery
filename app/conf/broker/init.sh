#!/bin/sh
( sleep 15 ; \
    rabbitmq-plugins enable rabbitmq_management
    #rabbitmq-plugins enable --offline rabbitmq_mqtt rabbitmq_federation_management rabbitmq_stomp

    rabbitmqctl add_user             $DEFAULT_USER $DEFAULT_PASS 2>/dev/null ; \
    rabbitmqctl set_user_tags        $DEFAULT_USER administrator; \
    rabbitmqctl set_permissions -p / $DEFAULT_USER  ".*" ".*" ".*" 
) &

exec docker-entrypoint.sh rabbitmq-server $@