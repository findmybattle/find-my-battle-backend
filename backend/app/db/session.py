from sqlmodel import SQLModel, create_engine, Session, delete, select

postgresql_file_name = "find_my_battle"
postgresql_url = (
    f"postgresql+psycopg://postgres:password@db:5432/{postgresql_file_name}"
)

engine = create_engine(postgresql_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    try:
        with Session(engine) as session:
            yield session
    finally:
        session.close()


def delete_all_rows(table_model: SQLModel):
    try:
        with Session(engine) as session:
            results = session.exec(select(table_model))
            session.delete(results)
            session.commit()
    except:
        print("No rows were deleted.")
    else:
        print("All rows deleted.")
