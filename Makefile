.PHONY: clean

OUT_HEADER=nuklear_preprocessed.h
SOURCE_HEADER=nuklear/nuklear.h

$(OUT_HEADER): $(SOURCE_HEADER)
	$(CC) -E -DNK_INCLUDE_VERTEX_BUFFER_OUTPUT -DNK_INCLUDE_DEFAULT_ALLOCATOR $(SOURCE_HEADER) > $(OUT_HEADER)
	sed -i '/_dummy_array/d' ./$(OUT_HEADER)

clean:
	-rm $(OUT_HEADER)
