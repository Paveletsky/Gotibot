import aiosqlite, asyncpg

class Database():
    def __init__(self, username, host, port, db_name, password):
        self._host = host
        self._port = port
        self._db_name: str = db_name
        self._username = username
        self._password = password
        self._db = None


    async def close(self):
        if isinstance(self._db, asyncpg.Connection):
            await self._db.close()


    async def GET(self) -> asyncpg.Connection:
        if isinstance(self._db, asyncpg.Connection):
            return self._db
                
        self._db = await asyncpg.connect(
            user     = self._username,
            password = self._password,
            host     = self._host,
            port     = self._port,
            database = self._db_name
        )

        await self._db.execute(
            """
            CREATE TABLE IF NOT EXISTS "aiogram_users"(
                "id" BIGINT NOT NULL PRIMARY KEY,
                "language" TEXT NOT NULL,
                "authcode" BIGINT
            )
            """
        ) 
        
        return self._db
    

    # USER FUNCS
    async def GetUser(self, id: int):
        data   = await self.GET()

        return bool(await data.fetchval(
            'SELECT * FROM "aiogram_users" WHERE "id" = $1', (id)
        ))


    async def AddUser(self, id: int, language: str = 'en'):
        data   = await self.GET()

        await data.execute(
            """
            INSERT INTO "aiogram_users" VALUES($1, $2)
            """
        , id, language)


    async def GetData(self, id: int, key: str):
        data   = await self.GET()
        result = await data.fetchrow(
            """
            SELECT * FROM "aiogram_users"
            WHERE "id" = $1
            """
        , id)

        return result[key] if result[key] else result


    async def SetData(self, id: int, key: str, info):
        data      = await self.GET()

        if key:
            await data.execute(
                f"""
                UPDATE "aiogram_users"
                SET "{key}" = $2
                WHERE "id" = $1
                """
            , id, info)
        else: return


    async def SetLanguage(self, id: int, lang: str = 'en'):
        data   = await self.GET()
        
        if lang:
            await data.execute(
                f"""
                UPDATE "aiogram_users"
                SET language = $1
                WHERE id = $2
                """
            , lang, id)
        else: return