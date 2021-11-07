import React, { useEffect, useState } from "react";
import { Heading, Flex, Divider } from "@chakra-ui/core";


const MessageContext = React.createContext({
  message: [], fetchMessage: () => {}
})

export default function Message() {
  const [message, setMessage] = useState([])
  const fetchMessage = async () => {
    // const response = await fetch("http://localhost:8000/todo")
    const response = await fetch("http://localhost:8080/")
    const message = await response.json()
    setMessage(message.message)
  }
  useEffect(() => {
    fetchMessage()
  }, [])
  return (
    <MessageContext.Provider value={{message, fetchMessage}}>
      <Flex
      as="nav"
      align="center"
      justify="space-between"
      wrap="wrap"
      padding="rem"
      bg="gray.400"
    >
      <Flex align="center" mr={5}>
        <Heading as="h1" size="sm"><b>Wiadomość z API: {message}</b></Heading>
        <Divider />
      </Flex>
    </Flex>
    </MessageContext.Provider>
  )
}
