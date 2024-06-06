from prisma.models import Collection

Collection.create_partial(name="CollectionSubFields", include={"id", "user_id", "action"})