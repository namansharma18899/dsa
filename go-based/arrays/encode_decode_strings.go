package main

import "encoding/base64"

type Codec struct {
}

func (codec *Codec) Encode(strs []string) string {
	encodedString := base64.StdEncoding.EncodeToString([]byte("your string"))
	return encodedString
}

func (codec *Codec) Decode(strs []string) []string {
	result := make([]string, 0)
	for _, each := range strs {
		decodedString, _ := base64.StdEncoding.DecodeString(each)
		result = append(result, string(decodedString))
	}
	return result
}
