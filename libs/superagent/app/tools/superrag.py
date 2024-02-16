import logging

from langchain_community.tools import BaseTool

from app.utils.helpers import get_superrag_compatible_credentials
from app.utils.prisma import prisma
from app.vectorstores.base import vector_db_mapping
from services.superrag import SuperRagService

logger = logging.getLogger(__name__)


class SuperRagTool(BaseTool):
    name = "superrag"
    description = "useful for when you need to answer questions"
    return_direct = False
    superrag_service = SuperRagService()

    def _run(
        self,
        question: str,
    ) -> str:
        """Use the tool."""
        pass

    async def _arun(
        self,
        question: str,
    ) -> str:
        """Use the tool asynchronously."""
        index_name = self.metadata.get("index_name")
        encoder = self.metadata.get("encoder")
        vector_database = self.metadata.get("vector_database")
        api_user_id = self.metadata.get("user_id")

        # with lower case e.g. pinecone, qdrant
        database_provider = vector_database.get("type")

        provider = await prisma.vectordb.find_first(
            where={
                "provider": vector_db_mapping.get(database_provider),
                "apiUserId": api_user_id,
            }
        )

        credentials = get_superrag_compatible_credentials(provider.options)

        return self.superrag_service.query(
            {
                "vector_database": {"type": database_provider, "config": credentials},
                "index_name": index_name,
                "encoder": encoder,
                "input": question,
            }
        )