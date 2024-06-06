import prisma
from prisma import Prisma

prisma_client: Prisma = Prisma()
prisma.register(prisma_client)