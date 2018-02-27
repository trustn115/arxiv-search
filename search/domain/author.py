"""Representations of authors, author lists, and author queries."""
from search.domain import Query, Property, Base


class Author(Base):
    """Represents an author."""

    forename = Property('forename', str)
    surname = Property('surname', str)
    fullname = Property('fullname', str)

    # TODO: gawd this is ugly.
    def __str__(self) -> str:
        """Print the author name."""
        if self.fullname and self.surname:
            if self.forename:
                name = f'{self.forename}[f] {self.surname}[s]'
            else:
                name = f'{self.surname}[s]'
            name = f'{name} OR {self.fullname}'
        elif self.fullname:
            name = self.fullname
        else:
            if self.forename:
                name = f'{self.forename}[f] {self.surname}[s]'
            else:
                name = f'{self.surname}[s]'
        return name


class AuthorList(list):
    """Represents a list of authors."""

    def __str__(self) -> str:
        """Prints comma-delimited list of authors."""
        if len(self) == 0:
            return ''
        if len(self) > 1:
            return ' AND '.join([f"({str(au)})" for au in self])
        return str(self[0])


class AuthorQuery(Query):
    """Represents an author query."""

    authors = Property('authors', AuthorList)
