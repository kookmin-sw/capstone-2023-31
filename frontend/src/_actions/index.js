export const addWishList = (item) => {
	return {
    	type: "ADD_ITEM",
      payload: item
    }
}

export const deleteWishList = (items) => {
	return {
    	type: "DELETE_ITEM",
      payload: items
    }
}