const wishReducer = (state = [], action) => {
  switch (action.type) {
    case "ADD_ITEM":
      return [ ...state, action.payload ];

    case "DELETE_ITEM":
      const index = state.findIndex(item => item.id === action.payload);
      const newState = [...state];
      newState.splice(index, 1);
      
      return newState;
      
    default:
      return state;
  }
}

export default wishReducer;