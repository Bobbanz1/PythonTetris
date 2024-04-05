from abc import ABC, abstractmethod
from typing import Self
from PartType import PartType


class GenericDocument(ABC):
    def __init__(self) -> None:
        self._document_parts = []

    def __getitem__(self, index):
        return self._document_parts[index]

    def __len__(self):
        return len(self._document_parts)

    def add_heading1(self, text: str) -> None:
        add = (PartType.HEADING1, text)
        self._document_parts.append(add)
        return self

    def add_heading2(self, text: str) -> None:
        add = (PartType.HEADING2, text)
        self._document_parts.append(add)
        return self

    def add_heading3(self, text: str) -> None:
        add = (PartType.HEADING3, text)
        self._document_parts.append(add)
        return self

    def add_paragraph(self, text: str) -> None:
        add = (PartType.PARAGRAPH, text)
        self._document_parts.append(add)
        return self

    def add_codeblock(self, text: str) -> None:
        add = (PartType.CODEBLOCK, text)
        self._document_parts.append(add)
        return self

    def merge_indices(self, dst_index: int, *src_indices, sep="\n") -> Self:
        dest_in_list = self._document_parts[dst_index]
        if not isinstance(dest_in_list, tuple):
            raise TypeError(
                "We were given the wrong kind of value from inside the _document_parts, something is wrong!"
            )

        if dst_index in src_indices:
            raise ValueError

        type_dest = dest_in_list[0]
        str_dest = dest_in_list[1]
        temp_list = list(dict.fromkeys(src_indices))
        temp_list.sort()
        # Loop through the given source indices and add the values to the str_dest.
        for stuff in temp_list:
            src_stuff = self._document_parts[stuff]
            str_dest = str_dest + sep + src_stuff[1]

        # Here we piece together a tuple from the values we have gotten out of type_dest and str_dest
        # In this case it should be the PartType alongside the joined together string.
        altering_tuple = (type_dest, str_dest)
        # print(self._document_parts)
        # Replace the entry the dst_index had with this new one.
        self._document_parts[dst_index] = altering_tuple
        # print(self._document_parts)
        # Here we need to sort the given list...or well make it into a list and then sort it so the highest value is first
        temp_list.sort(reverse=True)
        # Then we need to loop and remove these entries from the self._document_parts list.
        for removing in temp_list:
            self._document_parts.pop(removing)
        return self

    def merge_consecutive(self, partType: PartType, sep: str = "\n") -> Self:
        # What we need to do here
        # Make the code loop through the current _document_parts
        # Check how many of each PartTypes exist.
        # Other idea, idk do some stuff.
        existed = False
        for stuff in PartType:
            if partType == stuff:
                existed = True
                break

        # Check to see if we were actually given a valid partType, if not then throw a fit!
        if existed != True:
            raise TypeError("partType was just given a value that is not in PartType")

        last_thing = ""
        result_string = ""
        ball_dict = {}

        # Loop through the document parts we have so far
        for i in self._document_parts:
            # First loop, last_thing is empty, give it the first entry in the _document_parts.
            if last_thing == "":
                last_thing = i
                continue
            if last_thing[0] != partType:
                last_thing = i
                continue
            # If we have already encountered the partType in the past.
            if last_thing[0] == i[0]:
                if self._document_parts.index(last_thing) in ball_dict:
                    dict_list = list(ball_dict[self._document_parts.index(last_thing)])
                    dict_list.append(i)
                    ball_dict[self._document_parts.index(last_thing)] = tuple(dict_list)
                else:
                    ball_dict[self._document_parts.index(last_thing)] = (last_thing, i)
            elif last_thing[0] != i[0]:
                # The last_thing partType was not the same as the current one, therefore overwrite the variable with this new partType
                last_thing = i

        if len(ball_dict) > 0:
            for keys, values in ball_dict.items():
                # values = list(values)
                # values.sort(reverse=True)
                for entries in values:
                    # print(entries)
                    if entries in self._document_parts:
                        x = self._document_parts.index(entries)
                        self._document_parts.pop(x)
                        if result_string == "":
                            result_string = entries[1]
                        else:
                            result_string = result_string + sep + entries[1]
                if result_string != "":
                    altered_tuple = (partType, result_string)
                    self._document_parts.insert(keys, altered_tuple)
                    result_string = ""
                    # print(self._document_parts)
        return self

    def render(self) -> str:
        result = ""
        for things in self._document_parts:
            match things[0]:
                case PartType.HEADING1:
                    if hasattr(self, "render_heading1"):
                        render_heading1 = getattr(self, "render_heading1")
                        part_result = render_heading1(text=things[1])
                        result = result + part_result
                    else:
                        render_paragraph = getattr(self, "render_paragraph")
                        part_result = render_paragraph(text=things[1])
                        result = result + part_result
                case PartType.HEADING2:
                    if hasattr(self, "render_heading2"):
                        render_heading2 = getattr(self, "render_heading2")
                        part_result = render_heading2(text=things[1])
                        result = result + part_result
                    elif hasattr(self, "render_heading1"):
                        render_heading1 = getattr(self, "render_heading1")
                        part_result = render_heading1(text=things[1])
                        result = result + part_result
                    else:
                        render_paragraph = getattr(self, "render_paragraph")
                        part_result = render_paragraph(text=things[1])
                        result = result + part_result
                case PartType.HEADING3:
                    if hasattr(self, "render_heading3"):
                        render_heading3 = getattr(self, "render_heading3")
                        part_result = render_heading3(text=things[1])
                        result = result + part_result
                    elif hasattr(self, "render_heading2"):
                        render_heading2 = getattr(self, "render_heading2")
                        part_result = render_heading2(text=things[1])
                        result = result + part_result
                    elif hasattr(self, "render_heading1"):
                        render_heading1 = getattr(self, "render_heading1")
                        part_result = render_heading1(text=things[1])
                        result = result + part_result
                    else:
                        render_paragraph = getattr(self, "render_paragraph")
                        part_result = render_paragraph(text=things[1])
                        result = result + part_result
                case PartType.PARAGRAPH:
                    if hasattr(self, "render_paragraph"):
                        render_paragraph = getattr(self, "render_paragraph")
                        part_result = render_paragraph(text=things[1])
                        result = result + part_result
                    else:
                        raise ValueError
                case PartType.CODEBLOCK:
                    if hasattr(self, "render_codeblock"):
                        render_codeblock = getattr(self, "render_codeblock")
                        part_result = render_codeblock(text=things[1])
                        result = result + part_result
                    else:
                        render_paragraph = getattr(self, "render_paragraph")
                        part_result = render_paragraph(text=things[1])
                        result = result + part_result

        return result

    @abstractmethod
    def render_paragraph(text) -> str:
        pass
