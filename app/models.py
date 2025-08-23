import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class Bible(db.Model):
    __tablename__ = "bible"
    id:so.Mapped[int] = so.mapped_column(primary_key=True)
    book:so.Mapped[str] = so.mapped_column(sa.String(50), index=True, nullable=False)
    chapter:so.Mapped[int] = so.mapped_column(sa.Integer(), index=True, nullable=False)
    verse:so.Mapped[int] = so.mapped_column(sa.Integer(), index=True, nullable=False)
    text:so.Mapped[str] = so.mapped_column(sa.String())
    translation:so.Mapped[str] = so.mapped_column(sa.String(20), index=True)
    book_code:so.Mapped[str] = so.mapped_column(sa.String(20), index=True)

    def __repr__(self):
        return f"<{self.book_code} - {self.book}>"